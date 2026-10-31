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
  A library facet is a grouping of characteristics unique to a suite of data and programming code that is used to develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LibraryFacet extends Facet {

  private String libraryType;


}