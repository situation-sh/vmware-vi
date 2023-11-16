# OvfFile

Represents a file that the caller has downloaded and stored somewhere appropriate.  An instance of this class is used to tell OvfManager about the choices the caller made about a file. This information is needed when the OVF descriptor is generated with createDescriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The ID of the device backed by this file.  This ID uniquely identifies the device within the entity hierarchy.  The caller will have received this along with the URL needed to download the file (this is handled by another service interface).  ***Since:*** vSphere API 4.0  | 
**path** | **str** | The path chosen by the caller for this file.  This path becomes the value of the \&quot;href\&quot; attribute of the corresponding \&quot;File\&quot; element in the OVF descriptor.  This path must be relative to the path chosen for the OVF descriptor. This implies that the caller must decide in advance on the path to which it will write the OVF descriptor, once it is returned.  The folder separator must be \&quot;/\&quot; (forward slash).  The path must not begin with a slash - ie. it must not be an absolute path.  ***Since:*** vSphere API 4.0  | 
**compression_method** | **str** | The compression method the caller chose to employ for this file.  ***Since:*** vSphere API 4.0  | [optional] 
**chunk_size** | **int** | The chunksize chosen by the caller.  When using chunking, the caller must adhere to the method described in the OVF specification.  ***Since:*** vSphere API 4.0  | [optional] 
**size** | **int** | The file size, as observed by the caller during download.  ***Since:*** vSphere API 4.0  | 
**capacity** | **int** | The capacity of the disk backed by this file.  This should only be set if the device backed by this file is a disk. This value will be written in the \&quot;capacity\&quot; attribute of the corresponding \&quot;Disk\&quot; element in the OVF descriptor.  Note that the \&quot;capacity\&quot; attribute is normally set to the capacity of the corresponding *VirtualDisk*. Setting this variable overrides the capacity from the VirtualDisk.  ***Since:*** vSphere API 4.1  | [optional] 
**populated_size** | **int** | The populated size of the disk backed by this file.  This should only be set if the device backed by this file is a disk. This value will be written in the \&quot;populatedSize\&quot; attribute of the corresponding \&quot;Disk\&quot; element in the OVF descriptor.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.ovf_file import OvfFile

# TODO update the JSON string below
json = "{}"
# create an instance of OvfFile from a JSON string
ovf_file_instance = OvfFile.from_json(json)
# print the JSON string representation of the object
print OvfFile.to_json()

# convert the object into a dict
ovf_file_dict = ovf_file_instance.to_dict()
# create an instance of OvfFile from a dict
ovf_file_form_dict = ovf_file.from_dict(ovf_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


