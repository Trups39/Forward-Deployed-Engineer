from strategies import BulkyPackageStrategy, HeavyPackageStrategy, PackageSorter

def sort(width, height, length, mass):
    sorter = PackageSorter(BulkyPackageStrategy())
    if sorter.sort(width, height, length, mass):
        sorter.set_strategy(HeavyPackageStrategy())  # Now check heavy after bulky
        if sorter.sort(width, height, length, mass):  # Check both bulky and heavy
            return "REJECTED"
        return "SPECIAL"
    sorter.set_strategy(HeavyPackageStrategy())
    if sorter.sort(width, height, length, mass):  # Check heavy for non-bulky packages
        return "SPECIAL"
    return "STANDARD"
