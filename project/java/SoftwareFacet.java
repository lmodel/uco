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
  A software facet is a grouping of characteristics unique to a software program (a definitively scoped instance of a collection of data or computer instructions that tell the computer how to work). [based on https://en.wikipedia.org/wiki/Software]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SoftwareFacet extends Facet {

  private String language;
  private Identity manufacturer;
  private String observableCpeid;
  private String observableSwid;
  private String observableVersion;


}