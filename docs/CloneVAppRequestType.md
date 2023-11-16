# CloneVAppRequestType

The parameters of *VirtualApp.CloneVApp_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new vApp.  | 
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VAppCloneSpec**](VAppCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.clone_v_app_request_type import CloneVAppRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CloneVAppRequestType from a JSON string
clone_v_app_request_type_instance = CloneVAppRequestType.from_json(json)
# print the JSON string representation of the object
print CloneVAppRequestType.to_json()

# convert the object into a dict
clone_v_app_request_type_dict = clone_v_app_request_type_instance.to_dict()
# create an instance of CloneVAppRequestType from a dict
clone_v_app_request_type_form_dict = clone_v_app_request_type.from_dict(clone_v_app_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


