# FaultDomainId

Represents the identity of a replication fault domain.  Fault domains IDs are globally unique.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the fault domain.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.fault_domain_id import FaultDomainId

# TODO update the JSON string below
json = "{}"
# create an instance of FaultDomainId from a JSON string
fault_domain_id_instance = FaultDomainId.from_json(json)
# print the JSON string representation of the object
print FaultDomainId.to_json()

# convert the object into a dict
fault_domain_id_dict = fault_domain_id_instance.to_dict()
# create an instance of FaultDomainId from a dict
fault_domain_id_form_dict = fault_domain_id.from_dict(fault_domain_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


