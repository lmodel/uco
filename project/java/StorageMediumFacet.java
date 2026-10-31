package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A storage medium facet is a grouping of characteristics unique to a the storage capabilities of a piece of equipment or a mechanism designed to serve a special purpose or perform a special function.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StorageMediumFacet extends Facet {

  private Integer totalStorageCapacityInBytes;


}