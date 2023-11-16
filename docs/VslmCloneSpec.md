# VslmCloneSpec

Specification of cloning a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name of the cloned virtual storage object.  ***Since:*** vSphere API 6.5  | 
**keep_after_delete_vm** | **bool** | Choice of the deletion behavior of this virtual storage object.  If not set, the default value is false.  ***Since:*** vSphere API 6.7  | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | The metadata KV pairs that are supposed to be updated on the destination virtual storage object.  The clone task is atomic by design. That being said, failing to update the specified metadata pairs leads to the failure of the clone task. If unset, no metadata will be updated. An empty string value is indicative of a vcenter tag.  ***Since:*** vSphere API 6.7.2  | [optional] 

## Example

```python
from vmware_vi.models.vslm_clone_spec import VslmCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmCloneSpec from a JSON string
vslm_clone_spec_instance = VslmCloneSpec.from_json(json)
# print the JSON string representation of the object
print VslmCloneSpec.to_json()

# convert the object into a dict
vslm_clone_spec_dict = vslm_clone_spec_instance.to_dict()
# create an instance of VslmCloneSpec from a dict
vslm_clone_spec_form_dict = vslm_clone_spec.from_dict(vslm_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


