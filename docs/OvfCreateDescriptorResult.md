# OvfCreateDescriptorResult

The result of creating the OVF descriptor for the entity.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_descriptor** | **str** | The OVF descriptor for the entity.  ***Since:*** vSphere API 4.0  | 
**error** | [**List[MethodFault]**](MethodFault.md) | Errors that happened during processing.  For example, unknown or unsupported devices could be found (in which case this array will contain one or more instances of Unsupported-/UnknownDevice).  ***Since:*** vSphere API 4.0  | [optional] 
**warning** | [**List[MethodFault]**](MethodFault.md) | Non-fatal warnings from the processing.  The result will be valid, but the user may choose to reject it based on these warnings.  ***Since:*** vSphere API 4.0  | [optional] 
**include_image_files** | **bool** | Returns true if there are ISO or Floppy images attached to one or more VMs.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.ovf_create_descriptor_result import OvfCreateDescriptorResult

# TODO update the JSON string below
json = "{}"
# create an instance of OvfCreateDescriptorResult from a JSON string
ovf_create_descriptor_result_instance = OvfCreateDescriptorResult.from_json(json)
# print the JSON string representation of the object
print OvfCreateDescriptorResult.to_json()

# convert the object into a dict
ovf_create_descriptor_result_dict = ovf_create_descriptor_result_instance.to_dict()
# create an instance of OvfCreateDescriptorResult from a dict
ovf_create_descriptor_result_form_dict = ovf_create_descriptor_result.from_dict(ovf_create_descriptor_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


