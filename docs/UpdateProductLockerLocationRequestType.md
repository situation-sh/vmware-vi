# UpdateProductLockerLocationRequestType

The parameters of *HostSystem.UpdateProductLockerLocation_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path for the VMware Tools repository on the host. It should have \&quot;/vmfs/volumes/\&quot; prefix and it should be a valid existing path, or it could be empty to restore to default value.  | 

## Example

```python
from vmware_vi.models.update_product_locker_location_request_type import UpdateProductLockerLocationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductLockerLocationRequestType from a JSON string
update_product_locker_location_request_type_instance = UpdateProductLockerLocationRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateProductLockerLocationRequestType.to_json()

# convert the object into a dict
update_product_locker_location_request_type_dict = update_product_locker_location_request_type_instance.to_dict()
# create an instance of UpdateProductLockerLocationRequestType from a dict
update_product_locker_location_request_type_form_dict = update_product_locker_location_request_type.from_dict(update_product_locker_location_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


