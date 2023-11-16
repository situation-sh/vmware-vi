# VslmRelocateSpec

Specification for relocating a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vslm_relocate_spec import VslmRelocateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmRelocateSpec from a JSON string
vslm_relocate_spec_instance = VslmRelocateSpec.from_json(json)
# print the JSON string representation of the object
print VslmRelocateSpec.to_json()

# convert the object into a dict
vslm_relocate_spec_dict = vslm_relocate_spec_instance.to_dict()
# create an instance of VslmRelocateSpec from a dict
vslm_relocate_spec_form_dict = vslm_relocate_spec.from_dict(vslm_relocate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


