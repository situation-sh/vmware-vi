# ArrayOfDvsTrafficRule

A boxed array of *DvsTrafficRule*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsTrafficRule]**](DvsTrafficRule.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_traffic_rule import ArrayOfDvsTrafficRule

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsTrafficRule from a JSON string
array_of_dvs_traffic_rule_instance = ArrayOfDvsTrafficRule.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsTrafficRule.to_json()

# convert the object into a dict
array_of_dvs_traffic_rule_dict = array_of_dvs_traffic_rule_instance.to_dict()
# create an instance of ArrayOfDvsTrafficRule from a dict
array_of_dvs_traffic_rule_form_dict = array_of_dvs_traffic_rule.from_dict(array_of_dvs_traffic_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


