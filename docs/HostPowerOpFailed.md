# HostPowerOpFailed

This fault is thrown when a host power operation fails.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_power_op_failed import HostPowerOpFailed

# TODO update the JSON string below
json = "{}"
# create an instance of HostPowerOpFailed from a JSON string
host_power_op_failed_instance = HostPowerOpFailed.from_json(json)
# print the JSON string representation of the object
print HostPowerOpFailed.to_json()

# convert the object into a dict
host_power_op_failed_dict = host_power_op_failed_instance.to_dict()
# create an instance of HostPowerOpFailed from a dict
host_power_op_failed_form_dict = host_power_op_failed.from_dict(host_power_op_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


