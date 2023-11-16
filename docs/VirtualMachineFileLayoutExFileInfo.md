# VirtualMachineFileLayoutExFileInfo

Basic information about a file.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | Key to reference this file.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of the file, including the complete datastore path.  ***Since:*** vSphere API 4.0  | 
**type** | **str** | Type of the file.  *VirtualMachineFileLayoutExFileType_enum* lists all valid values.  ***Since:*** vSphere API 4.0  | 
**size** | **int** | Size of the file in bytes.  ***Since:*** vSphere API 4.0  | 
**unique_size** | **int** | Size of the file in bytes corresponding to the file blocks that were allocated uniquely.  In other words, if the underlying storage supports sharing of file blocks across disk files, the property corresponds to the size of the file blocks that were allocated only in context of this file, i.e. it does not include shared blocks that were allocated in other files. This property will be unset if the underlying implementation is unable to compute this information. One example of this is when the file resides on a NAS datastore whose underlying storage doesn&#39;t support this metric. In some cases the field might be set but the value could be over-estimated due to the inability of the NAS based storage to provide an accurate value.  ***Since:*** vSphere API 5.1  | [optional] 
**backing_object_id** | **str** | Backing object&#39;s durable and unmutable identifier.  Each backing object has a unique identifier which is not settable. This property is applied to the file backed by a storage object, such as vvol.  ***Since:*** vSphere API 6.0  | [optional] 
**accessible** | **bool** | Flag which indicates the accessibility of the file when the file info object was created.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_ex_file_info import VirtualMachineFileLayoutExFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutExFileInfo from a JSON string
virtual_machine_file_layout_ex_file_info_instance = VirtualMachineFileLayoutExFileInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutExFileInfo.to_json()

# convert the object into a dict
virtual_machine_file_layout_ex_file_info_dict = virtual_machine_file_layout_ex_file_info_instance.to_dict()
# create an instance of VirtualMachineFileLayoutExFileInfo from a dict
virtual_machine_file_layout_ex_file_info_form_dict = virtual_machine_file_layout_ex_file_info.from_dict(virtual_machine_file_layout_ex_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


