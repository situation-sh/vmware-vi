# VslmCreateSpecBackingSpec

Specification of the backing of a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**path** | **str** | Relative location in the specified datastore where disk needs to be created.  If not specified disk gets created at the defualt VStorageObject location on the specified datastore.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.vslm_create_spec_backing_spec import VslmCreateSpecBackingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmCreateSpecBackingSpec from a JSON string
vslm_create_spec_backing_spec_instance = VslmCreateSpecBackingSpec.from_json(json)
# print the JSON string representation of the object
print VslmCreateSpecBackingSpec.to_json()

# convert the object into a dict
vslm_create_spec_backing_spec_dict = vslm_create_spec_backing_spec_instance.to_dict()
# create an instance of VslmCreateSpecBackingSpec from a dict
vslm_create_spec_backing_spec_form_dict = vslm_create_spec_backing_spec.from_dict(vslm_create_spec_backing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


