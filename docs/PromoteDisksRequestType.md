# PromoteDisksRequestType

The parameters of *VirtualMachine.PromoteDisks_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlink** | **bool** | If true, then these disks will be unlinked before consolidation.  | 
**disks** | [**List[VirtualDisk]**](VirtualDisk.md) | The set of disks that are to be promoted. If this value is unset or the array is empty, all disks which have delta disk backings are promoted.  | [optional] 

## Example

```python
from vmware_vi.models.promote_disks_request_type import PromoteDisksRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteDisksRequestType from a JSON string
promote_disks_request_type_instance = PromoteDisksRequestType.from_json(json)
# print the JSON string representation of the object
print PromoteDisksRequestType.to_json()

# convert the object into a dict
promote_disks_request_type_dict = promote_disks_request_type_instance.to_dict()
# create an instance of PromoteDisksRequestType from a dict
promote_disks_request_type_form_dict = promote_disks_request_type.from_dict(promote_disks_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


