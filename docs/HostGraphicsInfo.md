# HostGraphicsInfo

This data object type describes information about a single graphics device.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The device name.  ***Since:*** vSphere API 5.5  | 
**vendor_name** | **str** | The vendor name.  ***Since:*** vSphere API 5.5  | 
**pci_id** | **str** | PCI ID of this device composed of \&quot;bus:slot.function\&quot;.  ***Since:*** vSphere API 5.5  | 
**graphics_type** | **str** | Graphics type (@see GraphicsType).  ***Since:*** vSphere API 5.5  | 
**memory_size_in_kb** | **int** | Memory capacity of graphics device or zero if not available.  ***Since:*** vSphere API 5.5  | 
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Virtual machines using this graphics device.  ***Since:*** vSphere API 5.5  Refers instances of *VirtualMachine*.  | [optional] 

## Example

```python
from vmware_vi.models.host_graphics_info import HostGraphicsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostGraphicsInfo from a JSON string
host_graphics_info_instance = HostGraphicsInfo.from_json(json)
# print the JSON string representation of the object
print HostGraphicsInfo.to_json()

# convert the object into a dict
host_graphics_info_dict = host_graphics_info_instance.to_dict()
# create an instance of HostGraphicsInfo from a dict
host_graphics_info_form_dict = host_graphics_info.from_dict(host_graphics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


