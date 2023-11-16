# OvfDiskOrderConstraint

Class used to indicate that the Disks in a DiskSection was not defined in the same order as in the Reference section  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_disk_order_constraint import OvfDiskOrderConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDiskOrderConstraint from a JSON string
ovf_disk_order_constraint_instance = OvfDiskOrderConstraint.from_json(json)
# print the JSON string representation of the object
print OvfDiskOrderConstraint.to_json()

# convert the object into a dict
ovf_disk_order_constraint_dict = ovf_disk_order_constraint_instance.to_dict()
# create an instance of OvfDiskOrderConstraint from a dict
ovf_disk_order_constraint_form_dict = ovf_disk_order_constraint.from_dict(ovf_disk_order_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


