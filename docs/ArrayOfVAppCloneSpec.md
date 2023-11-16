# ArrayOfVAppCloneSpec

A boxed array of *VAppCloneSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppCloneSpec]**](VAppCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_clone_spec import ArrayOfVAppCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppCloneSpec from a JSON string
array_of_v_app_clone_spec_instance = ArrayOfVAppCloneSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppCloneSpec.to_json()

# convert the object into a dict
array_of_v_app_clone_spec_dict = array_of_v_app_clone_spec_instance.to_dict()
# create an instance of ArrayOfVAppCloneSpec from a dict
array_of_v_app_clone_spec_form_dict = array_of_v_app_clone_spec.from_dict(array_of_v_app_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


