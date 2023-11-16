# VirtualNVDIMMBackingInfo

The <code>*VirtualNVDIMMBackingInfo*</code> data object type defines information about a resource that backs a device in a virtual machine.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**VirtualNVDIMMBackingInfo**](VirtualNVDIMMBackingInfo.md) |  | [optional] 
**change_id** | **str** | The change ID of the virtual NVDIMM for the corresponding snapshot of virtual machine.  This can be used to track incremental changes. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_nvdimm_backing_info import VirtualNVDIMMBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVDIMMBackingInfo from a JSON string
virtual_nvdimm_backing_info_instance = VirtualNVDIMMBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualNVDIMMBackingInfo.to_json()

# convert the object into a dict
virtual_nvdimm_backing_info_dict = virtual_nvdimm_backing_info_instance.to_dict()
# create an instance of VirtualNVDIMMBackingInfo from a dict
virtual_nvdimm_backing_info_form_dict = virtual_nvdimm_backing_info.from_dict(virtual_nvdimm_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


