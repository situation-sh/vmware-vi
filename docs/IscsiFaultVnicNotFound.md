# IscsiFaultVnicNotFound

This fault indicates an attempt was made to add a non-existent Virtual NIC adapter.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_not_found import IscsiFaultVnicNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicNotFound from a JSON string
iscsi_fault_vnic_not_found_instance = IscsiFaultVnicNotFound.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicNotFound.to_json()

# convert the object into a dict
iscsi_fault_vnic_not_found_dict = iscsi_fault_vnic_not_found_instance.to_dict()
# create an instance of IscsiFaultVnicNotFound from a dict
iscsi_fault_vnic_not_found_form_dict = iscsi_fault_vnic_not_found.from_dict(iscsi_fault_vnic_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


