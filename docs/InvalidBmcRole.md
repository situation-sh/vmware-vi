# InvalidBmcRole

An InvalidBmcRole fault is thrown when a BMC user doesn't have the necessary privileges.  BMC (Board Management Controller) is a piece of hardware required for IPMI.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_bmc_role import InvalidBmcRole

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidBmcRole from a JSON string
invalid_bmc_role_instance = InvalidBmcRole.from_json(json)
# print the JSON string representation of the object
print InvalidBmcRole.to_json()

# convert the object into a dict
invalid_bmc_role_dict = invalid_bmc_role_instance.to_dict()
# create an instance of InvalidBmcRole from a dict
invalid_bmc_role_form_dict = invalid_bmc_role.from_dict(invalid_bmc_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


