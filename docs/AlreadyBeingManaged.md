# AlreadyBeingManaged

AlreadyBeingManaged fault is thrown by the host connect method if the host is already being managed by a VirtualCenter server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of server that is currently managing the host.  | 

## Example

```python
from vmware_vi.models.already_being_managed import AlreadyBeingManaged

# TODO update the JSON string below
json = "{}"
# create an instance of AlreadyBeingManaged from a JSON string
already_being_managed_instance = AlreadyBeingManaged.from_json(json)
# print the JSON string representation of the object
print AlreadyBeingManaged.to_json()

# convert the object into a dict
already_being_managed_dict = already_being_managed_instance.to_dict()
# create an instance of AlreadyBeingManaged from a dict
already_being_managed_form_dict = already_being_managed.from_dict(already_being_managed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


