# OvfCreateDescriptorParams

Collection of parameters for createDescriptor  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_files** | [**List[OvfFile]**](OvfFile.md) | Contains information about the files of the entity, if they have already been downloaded.  Needed to construct the References section of the descriptor.  OvfFile is a positive list of files to include in the export. An Empty list will do no filtering.  ***Since:*** vSphere API 4.0  | [optional] 
**name** | **str** | The ovf:id to use for the top-level OVF Entity.  If unset, the entity&#39;s product name is used if available. Otherwise, the VI entity name is used.  ***Since:*** vSphere API 4.0  | [optional] 
**description** | **str** | The contents of the Annontation section of the top-level OVF Entity.  If unset, any existing annotation on the entity is left unchanged.  ***Since:*** vSphere API 4.0  | [optional] 
**include_image_files** | **bool** | Controls whether attached image files should be included in the descriptor.  This applies to image files attached to VirtualCdrom and VirtualFloppy.  ***Since:*** vSphere API 4.1  | [optional] 
**export_option** | **List[str]** | An optional argument for modifying the export process.  The option is used to control what extra information that will be included in the OVF descriptor.  To get a list of supported keywords see *OvfManager.ovfExportOption*. Unknown options will be ignored by the server.  ***Since:*** vSphere API 5.1  | [optional] 
**snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.ovf_create_descriptor_params import OvfCreateDescriptorParams

# TODO update the JSON string below
json = "{}"
# create an instance of OvfCreateDescriptorParams from a JSON string
ovf_create_descriptor_params_instance = OvfCreateDescriptorParams.from_json(json)
# print the JSON string representation of the object
print OvfCreateDescriptorParams.to_json()

# convert the object into a dict
ovf_create_descriptor_params_dict = ovf_create_descriptor_params_instance.to_dict()
# create an instance of OvfCreateDescriptorParams from a dict
ovf_create_descriptor_params_form_dict = ovf_create_descriptor_params.from_dict(ovf_create_descriptor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


