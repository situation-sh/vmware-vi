# HostSpecification

The host specification data are those needed at host boot time to create and configure virtual devices and host services.  The *HostSpecification* data object contains a collection of host sub specification data. For host sub specification data, see *HostSubSpecification* for details.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | Time at which the host specification was created.  ***Since:*** vSphere API 6.5  | 
**last_modified** | **datetime** | Time at which the host specification was last modified.  If it isn&#39;t set, it is the same as &lt;code&gt;createdTime&lt;/code&gt;.  ***Since:*** vSphere API 6.5  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**sub_specs** | [**List[HostSubSpecification]**](HostSubSpecification.md) | The collection of the host sub specifications.  It is optional.  ***Since:*** vSphere API 6.5  | [optional] 
**change_id** | **str** | The change ID for querying the host specification data updated in a time period.  It has a format of timestamp:change\\_number, where timestamp is the decimal string of a start time, and change\\_number is the decimal string of an auto incremented variable counting from the start time.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_specification import HostSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of HostSpecification from a JSON string
host_specification_instance = HostSpecification.from_json(json)
# print the JSON string representation of the object
print HostSpecification.to_json()

# convert the object into a dict
host_specification_dict = host_specification_instance.to_dict()
# create an instance of HostSpecification from a dict
host_specification_form_dict = host_specification.from_dict(host_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


