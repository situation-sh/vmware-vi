# ArrayOfInvalidBmcRole

A boxed array of *InvalidBmcRole*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidBmcRole]**](InvalidBmcRole.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_bmc_role import ArrayOfInvalidBmcRole

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidBmcRole from a JSON string
array_of_invalid_bmc_role_instance = ArrayOfInvalidBmcRole.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidBmcRole.to_json()

# convert the object into a dict
array_of_invalid_bmc_role_dict = array_of_invalid_bmc_role_instance.to_dict()
# create an instance of ArrayOfInvalidBmcRole from a dict
array_of_invalid_bmc_role_form_dict = array_of_invalid_bmc_role.from_dict(array_of_invalid_bmc_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


