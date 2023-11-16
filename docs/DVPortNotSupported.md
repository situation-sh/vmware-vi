# DVPortNotSupported

The virtual machine is configured to use a DVPort, which is not supported on the host.  This could be because the host does not support VDS at all, or because the host has not joined a VDS.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dv_port_not_supported import DVPortNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortNotSupported from a JSON string
dv_port_not_supported_instance = DVPortNotSupported.from_json(json)
# print the JSON string representation of the object
print DVPortNotSupported.to_json()

# convert the object into a dict
dv_port_not_supported_dict = dv_port_not_supported_instance.to_dict()
# create an instance of DVPortNotSupported from a dict
dv_port_not_supported_form_dict = dv_port_not_supported.from_dict(dv_port_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


