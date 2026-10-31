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
  Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BirthInformationFacet extends IdentityFacet {

  private ZonedDateTime birthdate;


}