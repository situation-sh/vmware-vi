# OvfFileItem

An FileItem represents a file that must be uploaded by the caller when the inventory objects has been created in VI.  These objects are created by *ResourcePool.importVApp*.  Files can either be new files, in which case the \"create\" flag will be true, or updates to existing files in VI. The latter is used to support the OVF parentRef mechanism for Disks.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Uniquely identifies the device (disk, CD-ROM etc.) within the entity hierarchy.  When *ResourcePool.importVApp* is called to create the *VirtualMachine*s and *VirtualApp*s, it returns a map, device ID -&amp;gt; URL, of where to upload the backing files.  ***Since:*** vSphere API 4.0  | 
**path** | **str** | The path of the item to upload, relative to the path of the OVF descriptor.  ***Since:*** vSphere API 4.0  | 
**compression_method** | **str** | The compression method as specified by the OVF specification (for example \&quot;gzip\&quot; or \&quot;bzip2\&quot;).  ***Since:*** vSphere API 4.0  | [optional] 
**chunk_size** | **int** | The chunksize as specified by the OVF specification.  If this attribute is set, the \&quot;path\&quot; attribute is a prefix to each chunk of the complete file. For example, if chunksize is 2000000000 bytes, the actual files might be: myfile.000000000 (2000000000 bytes) myfile.000000001 (2000000000 bytes) myfile.000000002 (1500000000 bytes)  ***Since:*** vSphere API 4.0  | [optional] 
**size** | **int** | The complete size of the file, if it is specified in the OVF descriptor.  ***Since:*** vSphere API 4.0  | [optional] 
**cim_type** | **int** | The CIM type of the device for which this file provides backing.  For example, the value 17 means \&quot;Disk drive\&quot;.  ***Since:*** vSphere API 4.0  | 
**create** | **bool** | True if the item is not expected to exist in the infrastructure and should therefore be created by the caller (for example using HTTP PUT).  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_file_item import OvfFileItem

# TODO update the JSON string below
json = "{}"
# create an instance of OvfFileItem from a JSON string
ovf_file_item_instance = OvfFileItem.from_json(json)
# print the JSON string representation of the object
print OvfFileItem.to_json()

# convert the object into a dict
ovf_file_item_dict = ovf_file_item_instance.to_dict()
# create an instance of OvfFileItem from a dict
ovf_file_item_form_dict = ovf_file_item.from_dict(ovf_file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


