def goodVsEvil(good, evil):
    cg = good.split()
    ce = evil.split()
    wg = [1,2,3,3,4,10]
    we = [1,2,2,2,3,5,10]
    sg = sum([int(cg[i])*wg[i] for i in range(len(wg))])
    se = sum([int(ce[i])*we[i] for i in range(len(we))]) # a great eagle is worth less than a troll?! Your nerd cred is ruined, sir
    return "Battle Result: " + ("Good triumphs over Evil" if sg > se else "Evil eradicates all trace of Good" if sg < se else "No victor on this battle field")
