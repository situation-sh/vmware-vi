# DomainNotFound

Fault indicating that the domain controller for domainName cannot be reached.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The domain that cannot be accessed.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.domain_not_found import DomainNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of DomainNotFound from a JSON string
domain_not_found_instance = DomainNotFound.from_json(json)
# print the JSON string representation of the object
print DomainNotFound.to_json()

# convert the object into a dict
domain_not_found_dict = domain_not_found_instance.to_dict()
# create an instance of DomainNotFound from a dict
domain_not_found_form_dict = domain_not_found.from_dict(domain_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


