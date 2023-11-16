# DeviceBackedVirtualDiskSpec

Specification used to create a host device backed virtual disk  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The deviceName of the backing device  See also *ScsiLun*.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.device_backed_virtual_disk_spec import DeviceBackedVirtualDiskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceBackedVirtualDiskSpec from a JSON string
device_backed_virtual_disk_spec_instance = DeviceBackedVirtualDiskSpec.from_json(json)
# print the JSON string representation of the object
print DeviceBackedVirtualDiskSpec.to_json()

# convert the object into a dict
device_backed_virtual_disk_spec_dict = device_backed_virtual_disk_spec_instance.to_dict()
# create an instance of DeviceBackedVirtualDiskSpec from a dict
device_backed_virtual_disk_spec_form_dict = device_backed_virtual_disk_spec.from_dict(device_backed_virtual_disk_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


