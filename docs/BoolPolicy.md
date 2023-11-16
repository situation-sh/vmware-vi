# BoolPolicy

The boolean type of setting or configuration that may get an inherited value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | The boolean value that is either set or inherited.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.bool_policy import BoolPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of BoolPolicy from a JSON string
bool_policy_instance = BoolPolicy.from_json(json)
# print the JSON string representation of the object
print BoolPolicy.to_json()

# convert the object into a dict
bool_policy_dict = bool_policy_instance.to_dict()
# create an instance of BoolPolicy from a dict
bool_policy_form_dict = bool_policy.from_dict(bool_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


