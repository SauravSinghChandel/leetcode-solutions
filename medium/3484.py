class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")

        return self.resolve(a) + self.resolve(b)

    def resolve(self, a):
        if a[0].isalpha():
            return self.cells.get(a, 0)
        return int(a)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
