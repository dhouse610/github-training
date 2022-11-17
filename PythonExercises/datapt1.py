def Route(button_source, button_destination):
    numSources = 36
    numDests = 5
    sourceURL = []
    destURL = []
    signageList = ["signage 1", "signage 2", "signage 3"]
    displayList = ["Left Front", "Right Front", "Rear", "Right Side", "Desk"]

    for i in range(numSources):
        if i <= numDests:
            destURL.append(f"display{i}URL")
            sourceURL.append(f"sourceTuner{i}URL")
        elif numDests<i<=32:
            sourceURL.append(f"sourceTuner{i}URL")
        elif i > 32:
            if i==33:
                x = 1
                sourceURL.append(f"sourceSignage{x}URL")
            elif i==34:
                x = 2
                sourceURL.append(f"sourceSignage{x}URL")
            elif i==35:
                x = 3
                sourceURL.append(f"sourceSignage{x}URL")
    return



























