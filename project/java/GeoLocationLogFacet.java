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
  A geolocation log facet is a grouping of characteristics unique to a record containing geolocation tracks and/or geolocation entries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeoLocationLogFacet extends Facet {

  private ObservableObject application;
  private ZonedDateTime observableCreatedTime;


}