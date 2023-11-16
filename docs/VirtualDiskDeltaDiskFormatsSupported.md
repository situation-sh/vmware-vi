# VirtualDiskDeltaDiskFormatsSupported

Delta disk format supported for each datastore type.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_type** | **str** | Datastore type name  ***Since:*** vSphere API 5.1  | 
**delta_disk_format** | [**ChoiceOption**](ChoiceOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_disk_delta_disk_formats_supported import VirtualDiskDeltaDiskFormatsSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskDeltaDiskFormatsSupported from a JSON string
virtual_disk_delta_disk_formats_supported_instance = VirtualDiskDeltaDiskFormatsSupported.from_json(json)
# print the JSON string representation of the object
print VirtualDiskDeltaDiskFormatsSupported.to_json()

# convert the object into a dict
virtual_disk_delta_disk_formats_supported_dict = virtual_disk_delta_disk_formats_supported_instance.to_dict()
# create an instance of VirtualDiskDeltaDiskFormatsSupported from a dict
virtual_disk_delta_disk_formats_supported_form_dict = virtual_disk_delta_disk_formats_supported.from_dict(virtual_disk_delta_disk_formats_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


