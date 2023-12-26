import random
def madlib():
    inp=input("WRITE AN ADJECTIVE : ")
    list1=["Adorable","Brave","Calm","Daring","Eager"]
    list2=["Fierce","Gleaming"," Happy", "Innocent", "Jovial"," Kind"]
    list3=["Vibrant","Whimsical", "Xquisite", "Youthful","Zesty"]
    list4=["Luminous", "Mysterious"," Noble","Optimistic", "Playful"]
    co_1=random.choice(list1)
    co_2=random.choice(list2)
    co_3=random.choice(list3)
    co_4=random.choice(list4)
    mad=f"Nestled in nature's embrace, the beautiful mountains{co_1} \
    stand as timeless sentinels, their majestic peaks reaching towards\
    the heavens. Clad in blankets of lush greenery{co_2} or pristine snow, these geological\
    wonders paint a breathtaking portrait against the canvas of the sky. As the sun \
    graces the horizon, casting its warm hues upon the rugged slopes, the mountains \
    awaken with a ethereal glow. Their {co_3}silent grandeur evokes a sense of awe, inviting\
     wanderers to embark on a journey of discovery. Each crag and crevice tells a tale\
     of resilience, {inp}shaped by the hands of time and the forces of nature. The air at these\
     lofty altitudes is pure and crisp, a {co_4}refreshing elixir for those seeking solace in the\
     arms of tranquility. Whether shrouded in mist or standing tall under a canopy of stars, \
    the beautiful mountains beckon, offering a sanctuary where the soul finds solace and the spirit soars."
    print(mad)



