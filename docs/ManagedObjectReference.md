# ManagedObjectReference

The ManagedObjectReference data object type is a special-purpose data object. Commonly referred to as simply a \"reference\", \"MoRef\", \"MOR\", or other variations of this theme, instances of managed object references contain data that identifies specific server-side managed objects. Managed object references are typically one of the return types from a method invocation.  Managed object references are client application references to server-side managed objects. The client application uses ManagedObjectReference objects when it invokes operations on a server. A ManagedObjectReference is guaranteed to be unique and persistent during an object's lifetime. The reference persists after an object has moved within the inventory, across sessions, and across server restarts. If you remove an object, for example, a virtual machine, from the inventory, and then put it back, the reference changes. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MoTypesEnum**](MoTypesEnum.md) |  | 
**value** | **str** | A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;.  | 

## Example

```python
from vmware_vi.models.managed_object_reference import ManagedObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedObjectReference from a JSON string
managed_object_reference_instance = ManagedObjectReference.from_json(json)
# print the JSON string representation of the object
print ManagedObjectReference.to_json()

# convert the object into a dict
managed_object_reference_dict = managed_object_reference_instance.to_dict()
# create an instance of ManagedObjectReference from a dict
managed_object_reference_form_dict = managed_object_reference.from_dict(managed_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


