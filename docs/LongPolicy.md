# LongPolicy

The long integer type of setting or configuration that may get an inherited value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The boolean value that is either set or inherited.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.long_policy import LongPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of LongPolicy from a JSON string
long_policy_instance = LongPolicy.from_json(json)
# print the JSON string representation of the object
print LongPolicy.to_json()

# convert the object into a dict
long_policy_dict = long_policy_instance.to_dict()
# create an instance of LongPolicy from a dict
long_policy_form_dict = long_policy.from_dict(long_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


