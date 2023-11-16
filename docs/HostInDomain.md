# HostInDomain

Fault indicating that an operation cannot be performed while the host is part of a Windows domain.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_in_domain import HostInDomain

# TODO update the JSON string below
json = "{}"
# create an instance of HostInDomain from a JSON string
host_in_domain_instance = HostInDomain.from_json(json)
# print the JSON string representation of the object
print HostInDomain.to_json()

# convert the object into a dict
host_in_domain_dict = host_in_domain_instance.to_dict()
# create an instance of HostInDomain from a dict
host_in_domain_form_dict = host_in_domain.from_dict(host_in_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


