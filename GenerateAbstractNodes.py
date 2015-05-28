
# coding: utf-8

# In[1]:

abstract = "Background: Cognitive impairment is a distressing, disruptive, and potentially debilitating symptom that can occur as a direct result of cancer or its treatment. National organizations have identified cognitive impairment as a challenge many survivors face and call for research to address this problem. Despite the priority, research is still relatively limited and questions remain unanswered about prevalence and impact on survivors, as well as coping strategies and effective treatment options available to address this potentially debilitating problem. Objectives: The purpose of this article is to (a) analyze the prevalence and types of cognitive impairment that commonly affect survivors; (b) delineate the impact that cognitive impairment after cancer and cancer treatment has on self-esteem, social relationships, work ability, and overall quality of life among survivors; and (c) synthesize and appraise commonly used coping strategies used by survivors to address cognitive impairment and evidence-based interventions that may be incorporated into clinical practice. Methods: A comprehensive review and synthesis of the literature was conducted. Findings: Evidence-based interventions to address cognitive changes after cancer and cancer treatment are limited. However, emerging research has demonstrated that nonpharmacologic treatments, such as cognitive training, are likely to be effective."


# In[2]:

print(abstract)


# In[30]:

list_of_proxies = []
dict_of_characters = {}

abstract_dict = {
      "@id": "https://scholarworks.iupui.edu/handle/1805/6451#Abstract",
      "pcdm:hasMember": [],
}

for index, abstract_character in enumerate(abstract):

    character_dict = {
        "@id": "https://scholarworks.iupui.edu/handle/1805/6451#UnicodeCharacterU+00{:X}".format(ord(abstract_character)),
        "rdf:label" : abstract_character
    }

    abstract_dict["pcdm:hasMember"].append(character_dict["@id"])

    dict_of_characters[abstract_character] = character_dict

    proxy = {
        "@id":"https://scholarworks.iupui.edu/handle/1805/6451#AbstractCharacter{}".format(index),
        "ore:proxyFor": character_dict["@id"],
        "ore:proxyIn": "https://scholarworks.iupui.edu/handle/1805/6451#Abstract"
    }

    if index == 0:
        abstract_dict["iana:first"] = proxy["@id"]
    else:
        proxy["iana:previous"] = list_of_proxies[index-1]["@id"]
        list_of_proxies[index-1]["iana:next"] = proxy["@id"]

    if index == (len(abstract) - 1):
        abstract_dict["iana:last"] = proxy["@id"]
        
    list_of_proxies.append(proxy)





# In[39]:

import json

print("{")
print('  "@id:":"{}",'.format(abstract_dict['@id']))
print('  "iana:first":"{}",'.format(abstract_dict["iana:first"]))
print('  "iana:first":"{}",'.format(abstract_dict["iana:last"]))
for elem in abstract_dict["pcdm:hasMember"]:
    print('  "pcdm:hasMember":"{}",'.format(elem))
print("},")

for prox in list_of_proxies:
    print("{},".format(json.dumps(prox)))
   
for charact in dict_of_characters.values():
    print("{},".format(json.dumps(charact)))


# In[ ]:



