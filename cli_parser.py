import argparse
from crud import add_expense, update_expense, delete_expense,list_expense,sum_expense

def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command',required=True)
   

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--description',required=True)
    add_parser.add_argument('--amount',required=True)
    add_parser.set_defaults(func=add_expense)

    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('--id',required=True)
    update_parser.add_argument('--description')
    update_parser.add_argument('--amount')
    update_parser.set_defaults(func=update_expense)

    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('--id',required=True)
    delete_parser.set_defaults(func=delete_expense)

    list_parser = subparsers.add_parser('list')
    list_parser.set_defaults(func=list_expense)

    sum_parser = subparsers.add_parser('summary')
    sum_parser.add_argument('--month')
    sum_parser.set_defaults(func=sum_expense)

    args = parser.parse_args()
    args.func(args)