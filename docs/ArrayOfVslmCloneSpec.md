# ArrayOfVslmCloneSpec

A boxed array of *VslmCloneSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VslmCloneSpec]**](VslmCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vslm_clone_spec import ArrayOfVslmCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVslmCloneSpec from a JSON string
array_of_vslm_clone_spec_instance = ArrayOfVslmCloneSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVslmCloneSpec.to_json()

# convert the object into a dict
array_of_vslm_clone_spec_dict = array_of_vslm_clone_spec_instance.to_dict()
# create an instance of ArrayOfVslmCloneSpec from a dict
array_of_vslm_clone_spec_form_dict = array_of_vslm_clone_spec.from_dict(array_of_vslm_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


