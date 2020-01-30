class Max_Difference:
    def __init__(self, list_of_nums, diff):
        self.list_of_nums = list_of_nums
        self.diff = diff

    def get_list(self):
        self.list_of_nums = list(map(int, input("Input the set of numbers you want to check: ").strip().split()))
        print(self.list_of_nums)

    def find_max_diff(self):
        diff = abs(max(self.list_of_nums) - min(self.list_of_nums))
        print("The max difference is " + str(diff))


max_diff = Max_Difference([], 2)
max_diff.get_list()
max_diff.find_max_diff()
