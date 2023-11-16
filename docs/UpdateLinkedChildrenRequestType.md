# UpdateLinkedChildrenRequestType

The parameters of *VirtualApp.UpdateLinkedChildren*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_change_set** | [**List[VirtualAppLinkInfo]**](VirtualAppLinkInfo.md) | a set of LinkInfo objects that either add a new link or modify an exisiting link.  ***Since:*** vSphere API 4.1  | [optional] 
**remove_set** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | a set of entities that should no longer link to this vApp.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.update_linked_children_request_type import UpdateLinkedChildrenRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLinkedChildrenRequestType from a JSON string
update_linked_children_request_type_instance = UpdateLinkedChildrenRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateLinkedChildrenRequestType.to_json()

# convert the object into a dict
update_linked_children_request_type_dict = update_linked_children_request_type_instance.to_dict()
# create an instance of UpdateLinkedChildrenRequestType from a dict
update_linked_children_request_type_form_dict = update_linked_children_request_type.from_dict(update_linked_children_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


