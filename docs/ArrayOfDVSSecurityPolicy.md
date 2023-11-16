# ArrayOfDVSSecurityPolicy

A boxed array of *DVSSecurityPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSSecurityPolicy]**](DVSSecurityPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_security_policy import ArrayOfDVSSecurityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSSecurityPolicy from a JSON string
array_of_dvs_security_policy_instance = ArrayOfDVSSecurityPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSSecurityPolicy.to_json()

# convert the object into a dict
array_of_dvs_security_policy_dict = array_of_dvs_security_policy_instance.to_dict()
# create an instance of ArrayOfDVSSecurityPolicy from a dict
array_of_dvs_security_policy_form_dict = array_of_dvs_security_policy.from_dict(array_of_dvs_security_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


