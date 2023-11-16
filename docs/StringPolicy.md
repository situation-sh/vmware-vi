# StringPolicy

The string type of setting or configuration that may get an inherited value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The String value that is either set or inherited.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.string_policy import StringPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StringPolicy from a JSON string
string_policy_instance = StringPolicy.from_json(json)
# print the JSON string representation of the object
print StringPolicy.to_json()

# convert the object into a dict
string_policy_dict = string_policy_instance.to_dict()
# create an instance of StringPolicy from a dict
string_policy_form_dict = string_policy.from_dict(string_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


