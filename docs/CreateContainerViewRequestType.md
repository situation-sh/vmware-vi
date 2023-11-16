# CreateContainerViewRequestType

The parameters of *ViewManager.CreateContainerView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**type** | **List[str]** | An optional list of managed entity types. The server associates only objects of the specified type(s) with the view. If you specify an empty array, the server uses all types.  | [optional] 
**recursive** | **bool** | Whether to include only the immediate children of the container instance, or to include additional objects by following paths beyond the immediate children.  When recursive is false, the list of objects contains only immediate children. When recursive is true, the server populates the list by following references beyond the immediate children (using a child&#39;s references, and then references in the resulting objects, and so on).  Depending on the container type, the server will use the following properties of the container instance to obtain objects for the view&#39;s object list: - *Folder* object - *Folder.childEntity*   property.   If recursive is false, the container list includes the reference   to the child entity in the folder instance.   If recursive is true, the server will follow the child   folder path(s) to collect additional childEntity references. - *ResourcePool* object - *ResourcePool.vm*   and *ResourcePool.resourcePool* properties.   If recursive is false, the object list will contain references   to the virtual machines associated with this resource pool,   and references to virtual machines associated with the   immediate child resource pools. If recursive is true,   the server will follow all child resource pool paths   extending from the immediate children (and their children,   and so on) to collect additional references to virtual machines. - *ComputeResource* object - *ComputeResource.host*   and *ComputeResource.resourcePool* properties.   If recursive is false, the object list will contain references   to the host systems associated with this compute resource,   references to virtual machines associated with the   host systems, and references to virtual machines associated   with the immediate child resource pools.   If recursive is true, the server will follow the child   resource pool paths (and their child resource pool paths,   and so on) to collect additional references to virtual machines. - *Datacenter* object - *Datacenter.vmFolder*,   *Datacenter.hostFolder*,   *Datacenter.datastoreFolder*, and   *Datacenter.networkFolder* properties.   If recursive is set to false, the server uses the   immediate child folders for the virtual machines,   hosts, datastores, and networks associated with this   datacenter. If recursive is set to true, the server   will follow the folder paths to collect references   to additional objects. - *HostSystem* object - *HostSystem.vm*   property.   The view object list contains references to the virtual machines   associated with this host system. The value of recursive does not   affect this behavior.  | 

## Example

```python
from vmware_vi.models.create_container_view_request_type import CreateContainerViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContainerViewRequestType from a JSON string
create_container_view_request_type_instance = CreateContainerViewRequestType.from_json(json)
# print the JSON string representation of the object
print CreateContainerViewRequestType.to_json()

# convert the object into a dict
create_container_view_request_type_dict = create_container_view_request_type_instance.to_dict()
# create an instance of CreateContainerViewRequestType from a dict
create_container_view_request_type_form_dict = create_container_view_request_type.from_dict(create_container_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


