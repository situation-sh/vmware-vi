# NotSupportedHostInDvs

A NotSupportedHostInDvs fault occurs when the host does not support the necessary features to participate in the DVS.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.not_supported_host_in_dvs import NotSupportedHostInDvs

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostInDvs from a JSON string
not_supported_host_in_dvs_instance = NotSupportedHostInDvs.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostInDvs.to_json()

# convert the object into a dict
not_supported_host_in_dvs_dict = not_supported_host_in_dvs_instance.to_dict()
# create an instance of NotSupportedHostInDvs from a dict
not_supported_host_in_dvs_form_dict = not_supported_host_in_dvs.from_dict(not_supported_host_in_dvs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


