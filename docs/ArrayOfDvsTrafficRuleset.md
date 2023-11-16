# ArrayOfDvsTrafficRuleset

A boxed array of *DvsTrafficRuleset*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsTrafficRuleset]**](DvsTrafficRuleset.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_traffic_ruleset import ArrayOfDvsTrafficRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsTrafficRuleset from a JSON string
array_of_dvs_traffic_ruleset_instance = ArrayOfDvsTrafficRuleset.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsTrafficRuleset.to_json()

# convert the object into a dict
array_of_dvs_traffic_ruleset_dict = array_of_dvs_traffic_ruleset_instance.to_dict()
# create an instance of ArrayOfDvsTrafficRuleset from a dict
array_of_dvs_traffic_ruleset_form_dict = array_of_dvs_traffic_ruleset.from_dict(array_of_dvs_traffic_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


