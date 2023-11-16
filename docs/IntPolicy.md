# IntPolicy

The integer type of setting or configuration that may get an inherited value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The integer value that is either set or inherited.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.int_policy import IntPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of IntPolicy from a JSON string
int_policy_instance = IntPolicy.from_json(json)
# print the JSON string representation of the object
print IntPolicy.to_json()

# convert the object into a dict
int_policy_dict = int_policy_instance.to_dict()
# create an instance of IntPolicy from a dict
int_policy_form_dict = int_policy.from_dict(int_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


