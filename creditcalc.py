import argparse
from math import log
from math import ceil


def get_interest(interest: float) -> float:
    return float(interest / (12 * 100))


#
def get_N(P: float, A: float, i: float) -> int:
    base = i + 1
    arg = A / (A - i * P)
    n = log(arg, base)
    return ceil(n)


def get_A(P: float, n: float, i: float) -> int:
    A = P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return ceil(A)


def get_P(A: float, n: float, i: float) -> int:
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return ceil(P)


def get_overpayment(P: float, A: float, n: float) -> None:
    print(f"Overpayment = {int((A * n) - P)}")


def get_Dm(P: float, n: float, i: float) -> None:
    payment_sum = 0
    for m in range(1, int(n + 1)):
        payment = ceil(P / n + (i * (P - ((P * (m - 1)) / n))))
        payment_sum += payment
        print(f"Month {m}: payment is {payment}")

    print(f"\nOverpayment = {int(payment_sum - P)}")


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--type", type=str, help="Interest rate"
    )
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Payment")
    parser.add_argument("--periods", type=float, help="Periods")
    parser.add_argument("--interest", type=float, help="Interest")

    args = parser.parse_args()
    if (
            args.interest is None
            or args.type is None
            or args.type not in ["annuity", "diff"]
            or args.interest < 0
            or args.principal is not None
            and args.principal < 0
            or args.payment is not None
            and args.payment < 0
            or args.periods is not None
            and args.periods < 0
    ):
        print("Incorrect parameters")

    elif args.type == "annuity":
        i: float = get_interest(args.interest)
        if args.periods is None:
            n: int = get_N(args.principal, args.payment, i)
            years: int = n // 12
            months: int = n % 12
            if years == 0:
                print(f"It will take {months} months to repay this loan!")

            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(
                    f"It will take {years} years and"
                    f" {months} months to repay this loan!"
                )
            get_overpayment(args.principal, args.payment, n)
        elif args.payment is None:
            A: int = get_A(args.principal, args.periods, i)
            print(f"Your monthly payment = {A}!")
            get_overpayment(args.principal, A, args.periods)
        else:
            P: int = get_P(args.payment, args.periods, i)
            print(f"Your loan principal = {P}!")
            get_overpayment(P, args.payment, args.periods)
    else:
        i: float = get_interest(args.interest)
        if args.periods is None or args.principal is None:
            print("Incorrect parameters")
        else:
            get_Dm(args.principal, args.periods, i)


if __name__ == "__main__":
    main()
